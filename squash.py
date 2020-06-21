# スカッシュゲーム（壁打ちテニス）

# モジュールのインポート
from tkinter import *

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 640, height = 480)
cv.pack()

# ゲームの初期化
def init_game():
    global is_gameover, ball_ichi_x, ball_ichi_y
    global ball_idou_x, ball_idou_y, ball_size
    global racket_ichi_x, racket_size, point, speed

    is_gameover = False
    ball_ichi_x = 0
    ball_ichi_y = 250
    ball_idou_x = 15
    ball_idou_y = -15
    ball_size = 10
    racket_ichi_x = 0
    racket_size = 100
    point = 0
    speed = 50
    win.title("スカッシュゲーム：スタート！")

# 画面の描画
def draw_screen():
    # 画面クリア
    cv.delete("all")
    # キャンバス(画面)の作成
    cv.create_rectangle(0, 0, 640, 480, fill = "white", width = 0)

def draw_ball():
    # ボールを描く
    cv.create_oval(ball_ichi_x - ball_size, ball_ichi_y - ball_size,
                   ball_ichi_x + ball_size, ball_ichi_y + ball_size, fill = "red")

def draw_racket():
    # ラケットを描く
    cv.create_rectangle(racket_ichi_x, 470,
                        racket_ichi_x + racket_size, 480, fill = "yellow")

# ボールの移動
def move_ball():
    global ball_ichi_x, ball_ichi_y, ball_idou_x, ball_idou_y

    if 0 <= ball_ichi_x + ball_idou_x <= 640:
        ball_ichi_x = ball_ichi_x + ball_idou_x
    if 0 <= ball_ichi_y + ball_idou_y <= 480:
        ball_ichi_y = ball_ichi_y + ball_idou_y

# ゲームの繰り返し処理
def game_loop():
    draw_screen()
    draw_ball()
    draw_racket()
    move_ball()
    win.after(speed, game_loop)


# ゲームのメイン処理
init_game()
game_loop()
win.mainloop()
