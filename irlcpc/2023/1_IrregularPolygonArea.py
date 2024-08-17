def question1(points: tuple[tuple[int, int]]):
    u: float = 0.0
    v: float = 0.0
    for i in range(len(points) - 1):
        point, next_point = points[i:i+2]
        u += point[0] * next_point[1]
        v += point[1] * next_point[0]
    area = abs(u - v)
    return area * 0.5

def main():
    print(question1(((0, 0), (0, 1), (1, 1), (1, 0))))
    print(question1(((0,0), (1,0), (0,1))))

if __name__ == "__main__":
    main()

