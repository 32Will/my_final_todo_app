import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    do = st.session_state['new_todo'] + '\n'
    todos.append(do)
    functions.write_todos(todos)


st.title('My todo App')
st.subheader('this is my todo App')
st.write('this app is to increase your productivity')

st.checkbox('Start Making money for Canada')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo",
              on_change=add_todo,
              key='new_todo')
