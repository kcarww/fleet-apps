import flet as ft 


def main(page: ft.Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window.maximized = True
    page.window.resizable = False
    
    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window.width - 10,
            height=page.window.height - 60,
            border_radius=10,
            
            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,
                    
                    content = ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            content = ft.Column([
                            ft.Text(
                                value='Sign In',
                                weight='bold',
                                size=20,
                                color=ft.colors.BLACK,
                                
                            )
                        ])
                        ),
                        ft.Column([
                            ft.TextField(
                                color=ft.colors.BLACK,
                                hint_text='Digite o seu email',
                                hint_style=ft.TextStyle(color=ft.colors.BLACK),
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),
                            
                            ft.TextField(
                                color=ft.colors.BLACK,
                                hint_text='Digite a sua senha',
                                hint_style=ft.TextStyle(color=ft.colors.BLACK),
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                can_reveal_password=True,
                                password=True,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),
                            
                            ft.ElevatedButton(
                                text='Sign in',
                                bgcolor=ft.colors.GREEN_500,
                                color=ft.colors.WHITE,
                                on_hover=ft.colors.BLACK,
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton(text='Recuperar conta'),
                                ft.TextButton(text='Criar nova conta')
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ], spacing=10),
                        
                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL),
                            ft.IconButton(icon=ft.icons.FACEBOOK),
                            ft.IconButton(icon=ft.icons.TELEGRAM),
                        ], alignment='center')
                        
                    ], horizontal_alignment='center')
                )
            ],horizontal_alignment='center', alignment='center')
        )
    ])
    
    register = ft.Column([
        
    ])
    
    page.add(login)


if __name__ == '__main__':
    ft.app(target=main)