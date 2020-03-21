
import simpy

class car(object) :
    def __init__(self,env):
        self.env = env
        self.action = env.process(self.run(env))


    def run(self,env):
        while True:
            print('Start parking at %d' % env.now)
            parking_duration = 5
            try :
                yield env.process(self.charge(env,parking_duration))
            except simpy.Interrupt :
                print('Was interrupted. Hope, the battery is full enough ...')

            print('Start traveling at %d ' % env.now)
            trip_duration = 2
            yield env.timeout(trip_duration)

    def charge(self,env,duration):
        yield env.timeout(duration)

def driver(env, car):
    yield env.timeout(3)
    car.action.interrupt()
