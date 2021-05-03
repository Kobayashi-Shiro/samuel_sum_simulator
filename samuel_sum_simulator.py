# -*- coding: utf-8 -*-

'''
The Samuel Sum Simulator (SSS) 
'''

import random as rd
from googlesearch import search
from re import compile as _Re

# splitting chi char
_unicode_chr_splitter = _Re('(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)').split

# store line no. to memory 
lines_mem = []  


class paragraph:
    '''
    Generate a paragraph based on a given detected keyword
    '''
    def __init__(self, detected_word):
        self.word = detected_word
        self.para = self.gen_para

    def gen_para(self): 
        ''' Match keyword to gen paragraph '''        
        if self.word == target_word_list[0]:  # 經濟
            possible_line_option_no = [1,2,3,7,8,9,10,12,13,16,17,20]  
        elif self.word == target_word_list[1]:  # 中美
            possible_line_option_no = [1,3,8,9,10,12,13,14,16]  
        elif self.word == target_word_list[2]:  # 中國
            possible_line_option_no = [1,2,3,7,8,9,10,15] 
        elif self.word == target_word_list[3]:  # 陰謀論
            possible_line_option_no = [2,4,5,6,10,11,12,13,14,15,16,18]  
        elif self.word == target_word_list[4] or \
            self.word == target_word_list[5]:  # 疫情
            possible_line_option_no = [1,2,3,7,8,11,12,19,20]              
   
        self.pick_lines(possible_line_option_no)
        print('\n')
    
    def pick_lines(self, possible_line_option_no):
        ''' Pick lines and call print funcs '''
        pick_amount = rd.choice(range(1,len(possible_line_option_no)))
        pick_lines_no = rd.sample(possible_line_option_no, k=pick_amount)  
        
        # check against mem to remove duplicated         
        pick_lines_no = [i for i in pick_lines_no if i not in lines_mem]        
        # store to mem
        lines_mem.extend(pick_lines_no)
        
        # call line_option func to print
        for line_no in pick_lines_no:
            eval('line_option_'+str(line_no)+'()')


def split_unicode_chrs(text):
    ''' Split chinese characters '''
    splitted_char = [chr for chr in _unicode_chr_splitter(text) if chr]
    
    return splitted_char


def read_input(input_text):
    ''' Detect keywords from input '''
    ind_input_words = split_unicode_chrs(input_text)
    
    detected_keyword_no = [] # to pick target_word_list index
    
    for input_word in ind_input_words:        
        for target_word_no, target_word in enumerate(target_word_list):
            ind_target_word = split_unicode_chrs(target_word)            
            for word in ind_target_word:                
                if word == input_word:
                    detected_keyword_no.append(target_word_no)
                    
    # Pick out words from target_word_list
    detected_keywords = [target_word_list[i] for i in set(detected_keyword_no)]

    return detected_keywords


def wiki(input_text):
    ''' Search wiki page'''
    search_line = 'wikipedia '+str(input_text)       
    results = search(search_line, tld='com', num=1, pause=0.001)      
    for result in results:  
        
        return result
    
    
def get_wiki_link(post_text):
    ''' Obtain a relevant wiki page '''
    wiki_result = wiki(post_text)
    word_shifter = 3 # remove some words
    while wiki_result is None:        
        ind_input_text = split_unicode_chrs(post_text)
        mod_input = ind_input_text[word_shifter:len(ind_input_text)]
        wiki_result = wiki([''.join(mod_input)])
        word_shifter += 2
    print(wiki_result)


# 語錄
def line_option_1():
    print('某人相信X爆論 \n而好多經濟財務學者不信')    
def line_option_2():
    print('已經精神病')
def line_option_3():
    print('唔睇經濟數據妄言X爆論')    
def line_option_4():
    print('教主之流只係一堆垃圾')    
def line_option_5():
    print('教主不死 \n係教徒殉教')    
def line_option_6():
    print('教主邪教徒')
def line_option_7():
    print('不影響經濟增長好困難')
def line_option_8():
    print('在香港金融分析員或經濟財務學者 \n無人會信')
def line_option_9():
    print('如果這叫政治')
def line_option_10():
    print('無獨立思考的人')    
def line_option_11():
    print('科學盲信病毒陰謀論')    
def line_option_12():
    print('都唔去 \n睇財經評論')    
def line_option_13():
    print('意識形態上腦')    
def line_option_14():
    print('是否陰謀論？')    
def line_option_15():
    print('陰謀論上腦')    
def line_option_16():
    print('有關中國崩潰論')    
def line_option_17():
    print('只是一班經濟盲學者')    
def line_option_18():
    print('腦有病')   
def line_option_19():
    print('都唔睇 \n科普文章')    
def line_option_20():
    print('經濟盲信X爆論')
        

def main():   
    print('Samuel Sum:\n')
    
    detected_keywords = read_input(input_text)
    for keyword in detected_keywords:
        comment = paragraph(keyword)
        comment.gen_para()
        
    get_wiki_link(input_text)


target_word_list = ['經濟','中美','中國','陰謀論','疫情','奕晴']
input_text = ''  ### INSERT POST TEXT


if __name__ == '__main__':
    main()




























