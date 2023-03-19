# 221RDB300

def parallel_processing(n, m, data):
    threads = [(i, 0) for i in range(n)]
    job_start_times = [None] * m
    for i in range(m):
        next_thread = min(threads, key=lambda x: x[1])
        threads[next_thread[0]] = (next_thread[0], next_thread[1] + data[i])
        job_start_times[i] = (next_thread[0], next_thread[1])

    output = [(job_start_times[i][0], job_start_times[i][1]) for i in range(m)]

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()