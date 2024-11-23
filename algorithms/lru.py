def lru_replacement(pages, frame_count):
    memory = []
    page_faults = 0
    results = []

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < frame_count:
                memory.append(page)
            else:
                # 找到最近最久未使用的页面
                last_used = []
                for m in memory:
                    last_used.append(pages[:i][::-1].index(m))
                memory.pop(last_used.index(max(last_used)))
                memory.append(page)
        else:
            # 如果页面已经在内存中，将其更新到最近使用
            memory.remove(page)
            memory.append(page)
        results.append(list(memory))
    return page_faults, results

