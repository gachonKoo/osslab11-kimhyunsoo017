from geo.utils import circle_circumference, circle_area

def main():
    r = 5
    c = circle_circumference(r)
    area = circle_area(r)

    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
