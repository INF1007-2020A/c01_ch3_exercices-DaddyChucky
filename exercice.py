import math


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs+angle_mins/60+angle_secs/3600)
    #return math.pi*(angle_degs+angle_mins/60+angle_secs/3600)/180


def to_degrees(angle_rads: float) -> tuple:
    deg = angle_rads/math.pi*180

    deg = deg - math.floor(angle_rads/math.pi*180)
    angle_mins = deg*60

    deg = angle_mins-math.floor(angle_mins)
    print(deg)
    angle_secs = deg*3600

    return round(deg,2), round(angle_mins,2), round(angle_secs,2)


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
