#指令：python -m\    /表情包网址：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
'''网页'''
import streamlit  as st
from PIL import Image
page = st.sidebar.radio("栏目",["首页","简介","作品","空间","聊天区"])
def img_change(img, rc, rg, rb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][rg]
            b = img_array[x, y][rb]
            img_array[x, y] = (r, g, b)
    return img
def page_1():
    if page == "首页":
        st.write("黑刃")
        st.write(":computer:工作室:computer:")
        st.write(":satellite_antenna:影刃工作室:satellite_antenna:")
        st.write("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        st.write(":chart:图片上传工具:chart:")
        uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
        if uploaded_file:
            file_name = uploaded_file.name
            file_type = uploaded_file.type
            file_size = uploaded_file.size
            img = Image.open(uploaded_file)
            st.image(img_change(img, 0, 1, 2))
            st.image(img)
            tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img, 0, 2, 1))
            with tab3:
                st.image(img_change(img, 1, 2, 0))
            with tab4:
                st.image(img_change(img, 1, 0, 2))
def page_2():  
    if page == "简介":
        st.write("影刃工作室")
        st.write("创办于：2021.6.5")
        st.write('作者：你猜')
        st.write('表情包网址：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')
        st.write('表情包网址可以在作品中的作品2那跳转')
def page_3():
    if page == "作品":
        st.write("作品1")
        st.write("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        st.write(":computer:词典（English）:computer:")
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')
        # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
        times_dict = {}
        for i in times_list:
            times_dict[i[0]] = int(i[1])
        # 创建输入框
        word = st.text_input('请输入要查询的单词（一次仅限一个单词）')
        # 显示查询内容
        if word in words_dict:
            st.write(words_dict[word][1])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = ""
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数',times_dict[n])
        st.write("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        st.write("作品2")
        st.write("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        name = st.text_input('网页名称')
        wangzhi = st.text_input('网址')
        go = st.selectbox('你要去哪？', ['百度', 'bilibili','表情包网址',name])
        if go == '百度':
            st.link_button('跳转到', 'https://www.baidu.com/')
        elif go == 'bilibili':
            st.link_button('跳转到', 'https://www.bilibili.com/')
        elif go == '表情包网址':
            st.link_button('跳转到', 'https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')
        elif go == name:
            st.link_button('跳转到',wangzhi)

def page_4():
    if page == "空间":
        st.write('前往作者的QQ空间→')
        st.link_button('作者的QQ空间','https://user.qzone.qq.com/')
        st.write("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        st.write('前往作者的b站主页→')
        st.link_button('作者的b站主页','https://space.bilibili.com/')
def page_5():
    if page == "聊天区":
        st.write("聊天区")
        name = name = st.text_input('你的名字')
        with open('leave_messages.txt','r',encoding='utf-8') as f:
            messages_list = f.read().split('\n')
        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split('#')
        for i in messages_list:
            if i[1] == '阿短':
                with st.chat_message('🐙'):
                    st.write(i[1],':',i[2])
            elif i[1] == '编程猫':
                with st.chat_message('🐧'):
                    st.write(i[1],':',i[2])
            elif i[1] == name:
                with st.chat_message(':computer:'):
                    st.write(i[1],':',i[2])
        name_list = st.selectbox('你是', ['阿短', '编程猫',name])
        new_message = st.text_input('想说的话')
        if st.button('留言'):
            messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
            with open('leave_messages.txt','w',encoding='utf-8') as f:
                message = ''
                for i in messages_list:
                    message += i[0] + '#' + i[1] + '#' +i[2] + '\n'
                message = message[:-1]
                f.write(message)

page_1()
page_2()
page_3()
page_4()
page_5()


