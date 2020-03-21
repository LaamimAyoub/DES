import simpy
from car_process import car, driver


def run_sim():
    env = simpy.Environment()
    m_car = car(env)
    env.process(driver(env, m_car))
    env.run(until=15)

if __name__ == '__main__':
    run_sim()