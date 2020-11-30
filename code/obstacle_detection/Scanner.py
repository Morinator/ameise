import pyrealsense2 as rs
import numpy as np


class Scanner:
    """ Handles the connection to the realsense camera and interprets its output.  """

    right, left, straight = range(3)

    # Initialize the Scanner. The value of limit defines the limit of the distance to objects that influence the
    # movement of the robot.
    def __init__(self, pipeline, limit=500):
        self.pipeline = pipeline
        self.pipeline.start()

		# define function that maps depth-values to true or false
        def map_to_boolean(x): return 0 < x < limit
        self.map_to_boolean = np.vectorize(map_to_boolean)

    # reads a current image and outputs a direction either left, right or straight
    def scan_output(self):
        height = 100  # the height of the sub-array that is scanned
        field_of_view = 150  # the length of the area that is scanned for obstacles

        # Create a pipeline object. This object configures the streaming camera and owns it's handle.
        frames = self.pipeline.wait_for_frames()
        depths = frames.get_depth_frame().get_data()
        depths = np.asarray(depths)

        dim = depths.shape  # should be 480 x 640
        height_half = dim[0]//2
        breadth_half = dim[1]//2
        field_of_view_half = field_of_view//2

		# cuts off the edges on the top and bottom sides of the depth-data
        depths = depths[range(height_half, dim[0], 2), :]
		
		# map all interesting values to true
        depths = self.map_to_boolean(depths)

        # group the depth-data into tree groups
		
        depths_left = depths[:, :breadth_half] # obstacles on the left
        depths_right = depths[:, breadth_half:] # obstacles on the right
		
		# obstacles in front of the robot, the robot will only continue straight if there aren't any obstacles in this group
        depths_straight = depths[:, breadth_half-field_of_view_half:breadth_half+field_of_view_half]

        if Scanner.count_true_in_matrix(depths_straight) > 0:
            if Scanner.count_true_in_matrix(depths_left) > Scanner.count_true_in_matrix(depths_right):
                return Scanner.right
            else:
                return Scanner.left
        else:
            return Scanner.straight

    # close the connection to the camera
    def close(self):
        self.pipeline.stop()

    # count how many times the value true appears in the given matrix
    def count_true_in_matrix(matrix):
        return len(list(filter(lambda x: x, matrix.reshape(-1))))

# start command line utility for testing purpose
def main():
	# initialize the device
    scanner = Scanner(rs.pipeline())

    switcher = {
        "read": scanner.scan_output
    }

    ''' 
    # command line loop
    # - if the user enters read the current image will be read and interpreted
    # - the output 0 means the robot should turn right, 1 means left and 2 means it should continue straight
    '''
	
    try:
        while True:
            user_input = input("> ")
            func = switcher.get(user_input)

            if callable(func):
                print(func())
            else:
                if user_input == "quit":
                    break
                else:
                    print("unknown command")

    finally:
        scanner.close()


if __name__ == '__main__':
    main()
