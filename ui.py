import tkinter as tk

root = tk.Tk(className="todo")

# todo一覧ラベル
todolab = tk.Label(text="ラベル")
todolab.pack()

# 入力テキストボックス
entertxtBox = tk.Entry()
entertxtBox.configure(state="normal", width=30)
entertxtBox.pack()

# 追加ボタン
addButton = tk.Button(text="追加", width=7)
addButton.bind(
    "<Button-1>",
)
addButton.pack()

# 期限のカレンダー


# 画面の表示
root.mainloop()
