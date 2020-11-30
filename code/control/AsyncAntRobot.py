from control.AntRobot import AntRobot
from concurrent.futures import ThreadPoolExecutor


# VERY IMPORTANT:
# This class allows it to run the movement-commands of the robot in a separate thread.
# However It is NOT ensured that a running command is executed completely before starting a new command.

class AsyncAntRobot(AntRobot):

    def __init__(self, port, baud_rate=2400, executor=ThreadPoolExecutor()):
        super().__init__(port, baud_rate)
        self.pool = executor
        self.futures = {}

    # ############## reset ##############
    # use the thread pool to run reset in a parallel and return the resulting future
    def reset(self):
        self.futures['reset'] = self.pool.submit(super().reset)  # run thread and save future-object
        if len(self.futures) > 1: self.clear_futures()         # if other futures a still in the dict, remove them if they are done
        return self.futures['reset']                             # return the future (not necessary)

    # wait for reset to finish
    def join_reset(self):
        if 'reset' in self.futures: self.__wait_for('reset')    # if a future object is present, wait for it's completion and delete it from the dict

    # ############## turn_left ##############
    # use the thread pool to run turn_left in a parallel and return the resulting future
    def turn_left(self, steps=1):
        self.futures['turn_left'] = self.pool.submit(super().turn_left, steps=steps)
        if len(self.futures) > 1: self.clear_futures()
        return self.futures['turn_left']

    # wait for turn_left to finish
    def join_turn_left(self):
        if 'turn_left' in self.futures: self.__wait_for('turn_left')

    # ############## turn_right ##############
    # use the thread pool to run turn_right in a parallel and return the resulting future
    def turn_right(self, steps=1):
        self.futures['turn_right'] = self.pool.submit(super().turn_right, steps=steps)
        if len(self.futures) > 1: self.clear_futures()
        return self.futures['turn_right']

    # wait for turn_right to finish
    def join_turn_right(self):
        if 'turn_right' in self.futures: self.__wait_for('turn_right')

    # ############## backwards ##############
    # use the thread pool to run backwards in a parallel and return the resulting future
    def backwards(self, steps=1):
        self.futures['backwards'] = self.pool.submit(super().backwards, steps=steps)
        if len(self.futures) > 1: self.clear_futures()
        return self.futures['backwards']

    # wait for backwards to finish
    def join_backwards(self):
        if 'backwards' in self.futures: self.__wait_for('backwards')

    # ############## forwards ##############
    # use the thread pool to run forwards in a parallel and return the resulting future
    def forwards(self, steps=1):
        self.futures['forwards'] = self.pool.submit(super().forwards, steps=steps)
        if len(self.futures) > 1: self.clear_futures()
        return self.futures['forwards']

    # wait for all actions to finish
    def join_action(self):
        keys = self.futures.copy().keys()
        for k in keys:
            self.__wait_for(k)

    # wait for forwards to finish
    def join_forwards(self):
        if 'forwards' in self.futures: self.__wait_for('forwards')

    # ############## other stuff ##############
    # wait for a future in the dictionary at position 'method_str' and delete it
    def __wait_for(self, method_str):
        self.futures[method_str].result()
        del self.futures[method_str]

    # method to clear completed tasks
    def clear_futures(self):
        keys = self.futures.copy().keys()
        for k in keys:
            if self.futures[k].done():
                del self.futures[k]
