import random
choice = random.choice

#在动物世界里，一只狮子的语言可以定义为
lion = """
lion = 自己 感觉 动作 标点
自己 = 我 | 大爷 | 幼仔子们 
感觉 = 困了 | 饿了
动作 = 要捕食 | 想睡觉 
标点 = ！ | 。
"""

#一只蚂蚁的语言可以定义为

ant = """
ant = 感叹 询问 结尾 
感叹 = 打招呼 | 惊叹 
打招呼 = 早上好，伙伴们 | 喂 | 还在干活啊
惊叹 = 快来看 | 我的天啊
询问 = 这是什么  
结尾 = ？ | ！
"""

def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

def generate(gram, target):
    if target not in gram: return target  # means target is a terminal expression

    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

def generate_n(gram,target,n):
    for i in range(n):
        print(generate(gram, target))
