# python3
# for each packet output the time start processing, or -1 if dropped
from collections import namedtuple

Response = namedtuple("Response", ["was_dropped", "started_at"])

class Request:
    def __init__(self, arrived_at, time_to_process):
        self.arrived_at = arrived_at
        self.time_to_process = time_to_process
        self.started_at = None
        self.ended_at = None


class Buffer:
    def __init__(self, size, total_requests):
        self.size = size
        self.finish_time = []
        self.requests = []
        self.total_requests = total_requests

    def process(self, request):
        dropped = False
        last_finish_time = self.finish_time[-1] if self.finish_time else 0
        request.started_at = max(last_finish_time, request.arrived_at)
        request.ended_at = request.started_at + request.time_to_process
        if self.size >= self.total_requests: # no need to drop
            self.requests.append(request)
            self.finish_time.append(request.ended_at)
            return Response(dropped, request.started_at)
        # drop if needed
        previous_requests = self.requests
        for r in self.requests:
            if request.arrived_at >= r.ended_at:
                previous_requests.remove(r)
        self.requests = previous_requests
        if len(previous_requests) >= self.size:
            dropped = True
            request.started_at = -1
            return Response(dropped, request.started_at)
        self.requests.append(request)
        self.finish_time.append(request.ended_at)
        return Response(dropped, request.started_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


PATH = "~/Downloads/starters_edx/week1_basic_data_structures_starters/network_packet_processing_simulation/tests"


def run(num):
    with open(f'{PATH}/{num}', 'r') as input_f:
        input = input_f.readlines()

    buffer_size, n_requests = map(int, input[0].split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input[1+_].split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size, n_requests)
    responses = process_requests(requests, buffer)

    f = open(f"{PATH}/{num}_output.txt", "a")
    for response in responses:
        f.write(str(response.started_at if not response.was_dropped else -1)+"\n")
    f.close()

    with open(f"{PATH}/{num}_output.txt", "r") as f:
        my_output = f.readlines()
    with open(f"{PATH}/{num}.a", "r") as f:
        output = f.readlines()
    for i in range(n_requests):
        if my_output[i] != output[i]:
            print("WRONG OUTPUT: ", str(i))
            print("my output: ", str(my_output[i]))
            print("correct output: ", str(output[i]))
            print("input: ", str(input[i + 1]))


if __name__ == "__main__":
    for i in range(1, 23):
        if len(str(i)) == 1:
            num = '0' + str(i)
        else:
            num = str(i)
        print('=== PROCESSING: ', num)
        run(num)
        print("=*" * 15)
