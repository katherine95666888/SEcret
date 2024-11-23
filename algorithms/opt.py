def opt_replacement(pages, frame_count):
    memory = []
    page_faults = 0
    results = []

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < frame_count:
                memory.append(page)
            else:
                # 找到未来最远被访问的页面
                future_use = []
                for m in memory:
                    try:
                        future_use.append(pages[i + 1:].index(m))
                    except ValueError:
                        future_use.append(float('inf'))
                memory.pop(future_use.index(max(future_use)))
                memory.append(page)
        results.append(list(memory))
    return page_faults, results

