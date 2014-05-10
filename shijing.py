print('诗经中最常见的诗句及其出现次数')

counter = {}

with open('23873-0.txt', encoding = 'utf-8') as shijing:
    for line in shijing:
        text = line.replace('、', '。')
        if text.find('。') == -1:
            continue
        texts = text.split('。')
        # 将中文诗句分隔符统一为句号并切句。
        
        for sentence in texts:
            if len(sentence) > 4:
                sentence = sentence.rstrip('兮')
            # 提取“XXXX兮”中的主要成分“XXXX”，如将“我心伤悲兮”也识别为“我心伤悲”这个句子。

            if sentence not in counter:
                counter[sentence] = 1
            else:
                counter[sentence] = counter[sentence] + 1
            # 统计诗句出现次数。
            
            
# 按诗句出现次数由高到低排序。
sentences = sorted(list(counter.items()), key = lambda e:e[1], reverse = True)
for i in range(10):
    if sentences[i][0].strip() == '':
    # 去掉换行符等干扰项，例如'\n'这种“诗句”。
        continue
    print('“{0}”出现了{1}次'.format(sentences[i][0], sentences[i][1]))


print()
print('诗经中最常见的诗句及其出现次数，同一首诗中重复的诗句计一次')

counter = {}
sentences = set()

with open('23873-0.txt', encoding = 'utf-8') as shijing:
    for line in shijing:
        if line.find('.  ') != -1:
            sentences = set()
        # 切换到新诗时，清空重复的诗句记录。
            
        text = line.replace('、', '。')
        if text.find('。') == -1:
            continue
        texts = text.split('。')
        # 将中文诗句分隔符统一为句号并切句。
        
        for sentence in texts:
            if len(sentence) > 4:
                sentence = sentence.rstrip('兮')
            # 提取“XXXX兮”中的主要成分“XXXX”，如将“我心伤悲兮”也识别为“我心伤悲”这个句子。
            
            if sentence in sentences:
                continue
            sentences.add(sentence)
            if sentence not in counter:
                counter[sentence] = 1
            else:
                counter[sentence] = counter[sentence] + 1
            # 统计诗句出现次数，不计同一首诗歌中重复的部分。
            
# 按诗句出现次数由高到低排序。
sentences = sorted(list(counter.items()), key = lambda e:e[1], reverse = True)
for i in range(10):
    if sentences[i][0].strip() == '':
        continue
    # 去掉换行符等干扰项，例如'\n'这种“诗句”。
    print('“{0}”出现在{1}首诗中'.format(sentences[i][0], sentences[i][1]))
