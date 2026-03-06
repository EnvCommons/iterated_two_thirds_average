from openreward.environments import Server

from env import IteratedTwoThirdsAverageEnvironment

if __name__ == "__main__":
    server = Server([IteratedTwoThirdsAverageEnvironment])
    server.run()
