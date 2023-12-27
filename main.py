from pyscript import document


def abc(event):
    input_text = document.querySelector("#english")
    input_text2 = document.querySelector("#uin")
    input_text.innerHTML=input_text2.value;
    print('Hello,World')
