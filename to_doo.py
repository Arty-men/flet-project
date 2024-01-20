import flet as ft

def main(page):
    def add_clicked(e):
        if new_task.value != '':
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()
    
    new_task = ft.TextField(hint_text="Done . . . ",
                            width=300)
    page.add(
        ft.Row([
            new_task, 
            ft.ElevatedButton("Add", 
                              on_click=add_clicked)
        ]))



if __name__ == '__main__':
    ft.app(target=main)