import pynvim
import jieba_fast as jieba


@pynvim.plugin
class Jieba(object):
    def __init__(self, vim):
        self.vim = vim
        self.calls = 0

    @pynvim.command('JiebaNextWord', range='', nargs='*', sync=True)
    def command_handler(self, args, range):
        win = 0
        line = self.vim.current.line
        cursor = self.vim.request('nvim_win_get_cursor', win)
        col = cursor[1] + 1
        next_col = self._get_next_chinese_word_col(line, col)
        self.vim.request('nvim_win_set_cursor', win, (cursor[0], next_col-1))

    def _get_next_chinese_word_col(self, line, col):
        words = jieba.lcut(line, HMM=False)
        sum = 1
        for i in range(len(words)):
            sum += len(words[i].encode('utf8'))
            if col < sum:
                return sum
        return sum

    def _is_chinese(self, line, col):
        pass
