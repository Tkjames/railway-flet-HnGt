import flet
from flet import ButtonStyle, Stack, colors, icons

from animated_menu_button import AnimatedMenuButton, MenuItem

def dummy_menu_handler(event):
    print("Clicked")

def main(page: Page):
    menu_items = [
        MenuItem(icon=icons.ADD_OUTLINED, handler=dummy_menu_handler),
        MenuItem(icon=icons.EDIT_OUTLINED, handler=dummy_menu_handler),
        MenuItem(icon=icons.INFO_OUTLINED, handler=dummy_menu_handler),
        MenuItem(
            icon=icons.DELETE_OUTLINE,
            handler=dummy_menu_handler,
            style=ButtonStyle(bgcolor=colors.ERROR_CONTAINER),
        ),
    ]

    page.add(Stack(expand=True, controls=[
        AnimatedMenuButton(menu_items, corner="top right", direction="curve down")
    ]))

    page.update()

# flet.app(target=main)


# import logging
# import flet as ft
# import os
# import matplotlib.pyplot as plt
# import numpy as np


# import flet as ft
# import matplotlib.pyplot as plt
# import numpy as np

# def main(page: ft.Page):
#     page.title = "Project Cost Calculator"
#     page.theme_mode = ft.ThemeMode.LIGHT  # Set theme to light for a clean look
#     page.padding = 20
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     def calculate_project_cost(hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier):
#         paid_hours = max(0, hours - pro_bono_hours)
#         subsidized_hours = min(paid_hours, subsidized_hours)
#         full_rate_hours = paid_hours - subsidized_hours

#         discounted_rate = rate * (1 - discount_rate)
#         cash_payment = (full_rate_hours * rate) + (subsidized_hours * discounted_rate)

#         if valuation > 0 and total_shares > 0:
#             equity_value_per_share = valuation / total_shares
#             equity_value = (equity_split / 100) * hours * rate / equity_value_per_share
#         else:
#             equity_value = 0
        
#         total_cost = (cash_payment + equity_value) * ip_multiplier
#         return total_cost, cash_payment, equity_value

#     def plot_project_cost():
#         hours = hours_slider.value
#         rate = rate_slider.value
#         equity_split = equity_slider.value
#         ip_ownership = ip_ownership_dropdown.value
#         pro_bono_hours = pro_bono_slider.value
#         subsidized_hours = subsidized_slider.value
#         discount_rate = discount_slider.value
#         valuation = valuation_slider.value
#         total_shares = shares_slider.value
        
#         ip_ownership_multipliers = {
#             "Full IP Ownership": 1.0,
#             "Joint IP Ownership": 0.9,
#             "No IP Ownership": 0.8
#         }
#         ip_multiplier = ip_ownership_multipliers[ip_ownership]
        
#         total_cost, cash_payment, equity_value = calculate_project_cost(
#             hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier
#         )

#         # Plotting
#         labels = ['Cash Payment', 'Equity Value']
#         values = [cash_payment, equity_value]
        
#         plt.figure(figsize=(6, 4))
#         plt.bar(labels, values, color=['#ff9999','#66b3ff'])
#         plt.title(f"Total Project Cost: ${total_cost:.2f}")
#         plt.ylabel('Amount in $')
        
#         plt_path = "/tmp/plot.png"
#         plt.savefig(plt_path)
#         plt.close()
        
#         chart_image.src = plt_path
#         chart_image.update()

#     # Header for Consultancy-style appearance
#     header = ft.Text(
#         "Project Cost Calculator",
#         size=32,
#         weight=ft.FontWeight.BOLD,
#         color=ft.colors.BLUE_GREY_900
#     )

#     # Sliders with labels
#     hours_slider = ft.Slider(min=10, max=100, value=20, label="Hours Worked", on_change=lambda _: plot_project_cost())
#     rate_slider = ft.Slider(min=50, max=200, value=120, label="Hourly Rate ($)", on_change=lambda _: plot_project_cost())
#     equity_slider = ft.Slider(min=0, max=100, value=50, label="Equity Split (%)", on_change=lambda _: plot_project_cost())
#     pro_bono_slider = ft.Slider(min=0, max=40, value=8, label="Pro Bono Hours", on_change=lambda _: plot_project_cost())
#     subsidized_slider = ft.Slider(min=0, max=40, value=8, label="Subsidized Hours", on_change=lambda _: plot_project_cost())
#     discount_slider = ft.Slider(min=0, max=0.5, value=0.1, label="Discount Rate (%)", on_change=lambda _: plot_project_cost())

#     # Dropdown for IP Ownership
#     ip_ownership_dropdown = ft.Dropdown(
#         label="IP Ownership",
#         options=[
#             ft.dropdown.Option("Full IP Ownership"),
#             ft.dropdown.Option("Joint IP Ownership"),
#             ft.dropdown.Option("No IP Ownership"),
#         ],
#         value="Full IP Ownership",
#         on_change=lambda _: plot_project_cost()
#     )

#     # Sliders for valuation and shares
#     valuation_slider = ft.Slider(min=100000, max=10000000, value=1000000, label="Valuation ($)", on_change=lambda _: plot_project_cost())
#     shares_slider = ft.Slider(min=1000, max=1000000, value=100000, label="Total Shares", on_change=lambda _: plot_project_cost())

#     # Image for the bar chart
#     chart_image = ft.Image()

#     # Organizing controls into a column for better visual appearance
#     sliders_col = ft.Column(
#         controls=[
#             header,
#             hours_slider,
#             rate_slider,
#             equity_slider,
#             ip_ownership_dropdown,
#             pro_bono_slider,
#             subsidized_slider,
#             discount_slider,
#             valuation_slider,
#             shares_slider
#         ],
#         spacing=15,
#         horizontal_alignment=ft.CrossAxisAlignment.STRETCH
#     )

#     # Adding a visual appealing layout
#     layout = ft.Column(
#         controls=[
#             sliders_col,
#             ft.Container(content=chart_image, alignment=ft.alignment.center, padding=20)
#         ],
#         spacing=30,
#         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         scroll=ft.ScrollMode.AUTO
#     )

#     page.add(layout)

#     # Initial plot
#     plot_project_cost()

# # Run the app
ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))


# # def main(page: ft.Page):
# #     page.title = "Project Cost Calculator"
    
# #     def calculate_project_cost(hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier):
# #         paid_hours = max(0, hours - pro_bono_hours)
# #         subsidized_hours = min(paid_hours, subsidized_hours)
# #         full_rate_hours = paid_hours - subsidized_hours

# #         discounted_rate = rate * (1 - discount_rate)
# #         cash_payment = (full_rate_hours * rate) + (subsidized_hours * discounted_rate)

# #         if valuation > 0 and total_shares > 0:
# #             equity_value_per_share = valuation / total_shares
# #             equity_value = (equity_split / 100) * hours * rate / equity_value_per_share
# #         else:
# #             equity_value = 0
        
# #         total_cost = (cash_payment + equity_value) * ip_multiplier
# #         return total_cost, cash_payment, equity_value

# #     def plot_project_cost():
# #         hours = hours_slider.value
# #         rate = rate_slider.value
# #         equity_split = equity_slider.value
# #         ip_ownership = ip_ownership_dropdown.value
# #         pro_bono_hours = pro_bono_slider.value
# #         subsidized_hours = subsidized_slider.value
# #         discount_rate = discount_slider.value
# #         valuation = valuation_slider.value
# #         total_shares = shares_slider.value
        
# #         ip_ownership_multipliers = {
# #             "Full IP Ownership": 1.0,
# #             "Joint IP Ownership": 0.9,
# #             "No IP Ownership": 0.8
# #         }
# #         ip_multiplier = ip_ownership_multipliers[ip_ownership]
        
# #         total_cost, cash_payment, equity_value = calculate_project_cost(
# #             hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier
# #         )

# #         # Plotting
# #         labels = ['Cash Payment', 'Equity Value']
# #         values = [cash_payment, equity_value]
        
# #         plt.figure(figsize=(6, 4))
# #         plt.bar(labels, values, color=['#ff9999','#66b3ff'])
# #         plt.title(f"Total Project Cost: ${total_cost:.2f}")
# #         plt.ylabel('Amount in $')
        
# #         plt_path = "/tmp/plot.png"
# #         plt.savefig(plt_path)
# #         plt.close()
        
# #         chart_image.src = plt_path
# #         chart_image.update()

# #     # Sliders
# #     hours_slider = ft.Slider(min=10, max=100, value=20, label="Hours", on_change=lambda _: plot_project_cost())
# #     rate_slider = ft.Slider(min=50, max=200, value=120, label="Hourly Rate ($)", on_change=lambda _: plot_project_cost())
# #     equity_slider = ft.Slider(min=0, max=100, value=50, label="Equity Split (%)", on_change=lambda _: plot_project_cost())
# #     pro_bono_slider = ft.Slider(min=0, max=40, value=8, label="Pro Bono Hours", on_change=lambda _: plot_project_cost())
# #     subsidized_slider = ft.Slider(min=0, max=40, value=8, label="Subsidized Hours", on_change=lambda _: plot_project_cost())
# #     discount_slider = ft.Slider(min=0, max=0.5, value=0.1, label="Discount (%)", on_change=lambda _: plot_project_cost())

# #     # Dropdown for IP Ownership
# #     ip_ownership_dropdown = ft.Dropdown(
# #         label="IP Ownership",
# #         options=[
# #             ft.dropdown.Option("Full IP Ownership"),
# #             ft.dropdown.Option("Joint IP Ownership"),
# #             ft.dropdown.Option("No IP Ownership"),
# #         ],
# #         value="Full IP Ownership",
# #         on_change=lambda _: plot_project_cost()
# #     )

# #     # Sliders for valuation and shares
# #     valuation_slider = ft.Slider(min=100000, max=10000000, value=1000000, label="Valuation ($)", on_change=lambda _: plot_project_cost())
# #     shares_slider = ft.Slider(min=1000, max=1000000, value=100000, label="Total Shares", on_change=lambda _: plot_project_cost())

# #     # Image for the bar chart
# #     chart_image = ft.Image()

# #     # Adding controls to the page
# #     page.add(
# #         hours_slider,
# #         rate_slider,
# #         equity_slider,
# #         ip_ownership_dropdown,
# #         pro_bono_slider,
# #         subsidized_slider,
# #         discount_slider,
# #         valuation_slider,
# #         shares_slider,
# #         chart_image,
# #     )

# #     # Initial plot
# #     plot_project_cost()

# # # Run the app

# # logging.basicConfig(level=logging.INFO)

# # ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
