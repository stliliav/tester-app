from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
from random import shuffle, randint
#класс question с параметрами вопроса
class Question():
    def __init__(self,question, right_answer, wrong1,wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
app = QApplication([])
main_win = QWidget()
#введение функций для отображения ответов и проверки результата
def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    btn_ok.setText('Ответить!')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
#создание функции для смены окон
def test():
    if btn_ok.text() == 'Ответить!':
        btn_ok.clicked.connect(show_result)
    else:
        btn_ok.clicked.connect(show_question)
#функция для определения конкретно правильного ответа и перемешивания вариантов
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Answer.setText('Правильный ответ:'+ q.right_answer)
    show_question()
#"реакция" на правильный или неправильный ответ
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    print('')
    if answers[0].isChecked():
        show_correct('Ура! Молодец!')
        main_win.score+=1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не угадал :0')

#переход к следующему вопросу
def next_question():
    main_win.total +=1
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

#обработка нажатия на кнопку ОК
def click_ok():
    if btn_ok.text() == 'Ответить!':
        check_answer()
    else:
        next_question()
#интерфейс       
main_win.setWindowTitle('Memory Card')
RadioGroupBox =QGroupBox('Варианты ответов')
#создание названия кнопок с 1 вариантом ответа
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
#cписок ответов
answers = [rbtn_1, rbtn_2,rbtn_3,rbtn_4]
RadioGroup = QButtonGroup()
#создание радио кнопок
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#задаем расположения виджетов
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
ansGroupBox= QGroupBox()
layout_reply = QVBoxLayout()
#задаем значения для прямоугольника, где отображается правильный ответ и реакция
lb_Answer =QLabel('Правильный ответ')
lb_Result =QLabel('Ответ:')
layout_reply.addWidget(lb_Answer)
layout_reply.addWidget(lb_Result)
ansGroupBox.setLayout(layout_reply)
btn_ok = QPushButton('Ответить!')
lb_Question = QLabel('Какой национальности не существует?')
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ansGroupBox)
RadioGroupBox.show()
ansGroupBox.hide()
layout_line3.addStretch(1)
#задать длину кнопки ОК
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.setSpacing(5)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
main_win.setLayout(layout_card)
main_win.cur_question = -1

main_win.total = 0
main_win.score = 0

main_win.show()
#создание вопросов
q1 = Question("Тангенса какого угла не существует?", '90', '180','45', '30')
q2 = Question("Чему равен корень из 729?", '27', '33','19', '29')
q3 = Question("Косинус какого угла равен 0,5?", '60', '45','30', '120')
q4 = Question("Чему равно произведение 12*34?", '408', '328','418', '224')
#объявление пустого списка, добавление в него вопросов и вариантов ответа
questions_list = []
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
#переход к следующему вопросу
next_question()
btn_ok.clicked.connect(click_ok)
app.exec_()