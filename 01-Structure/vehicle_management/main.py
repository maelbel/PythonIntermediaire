from rentals import rental_manager
from drivers import driver_manager
from vehicules import vehicle_manager


def main():

    driver = driver_manager.new_driver("Ted")

    car = vehicle_manager.new_vehicle("Renault")

    rental = rental_manager.new_rental(driver, car)

    print(rental)

if __name__ == "__main__":
    main()