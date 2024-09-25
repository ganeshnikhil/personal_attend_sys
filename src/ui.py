import gradio as gr
from src.ui_db_op import submit_attendance, display_database, month_dates

def main_gradio():
    # Get all available dates for selection
    dates = month_dates()

    # Ensure dates are not empty; add a fallback if needed
    if not dates:
        dates = ["No dates available"]

    with gr.Blocks() as demo:
        gr.Markdown("### Attendance Management System")

        # Dropdown to select a date
        date_input = gr.Dropdown(choices=dates, label="Select Date", interactive=True)

        # Radio buttons to select present or absent
        persent_input = gr.Radio(choices=["Present", "Absent"], label="Present or Absent", interactive=True)

        # Submit button to write attendance to the database
        submit_button = gr.Button("Submit Attendance")

        # Display the result after submission
        output_text = gr.Textbox(label="Output", interactive=False)

        # Data display button and output
        show_data_button = gr.Button("Show All Attendance Data")
        database_display = gr.Dataframe(headers=["ID", "Date", "Time", "Present"], value=[], row_count=5)

        # Action when "Submit Attendance" button is clicked
        submit_button.click(fn=submit_attendance, inputs=[date_input, persent_input], outputs=output_text)

        # Action to display database content when "Show All Attendance Data" button is clicked
        show_data_button.click(fn=display_database, inputs=None, outputs=database_display)

    return demo

if __name__ == "__main__":
    demo = main_gradio()
    demo.launch()
