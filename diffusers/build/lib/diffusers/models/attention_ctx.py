from collections import deque

class AttentionCtx:
  def __init__(self):
    self.cnt = 0
    self.attention_probs_list = deque(maxlen=2)

  def hello(self):
    self.cnt += 1
    print('hello', self.cnt)

  def collect_attention_probs(self, probs):
    self.attention_probs_list.append(probs)