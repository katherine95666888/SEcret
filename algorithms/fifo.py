from collections import deque

def fifo_replacement(pages, frame_count):
    memory = deque()
    page_faults = 0
    results = []

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frame_count:
                memory.append(page)
            else:
                memory.popleft()
                memory.append(page)
        results.append(list(memory))
    return page_faults, results

