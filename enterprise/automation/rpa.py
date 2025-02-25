import pyautogui
import time
import os

def automate_invoice_processing():
    """Automates form filling based on extracted invoice data"""
    
    # Simulate opening enterprise software (assumes it's already running)
    time.sleep(2)
    
    # Move cursor to invoice field and enter details
    pyautogui.click(x=400, y=300)  # Example coordinates
    pyautogui.write("Invoice ID: 123456")

    # Move to next field
    pyautogui.press("tab")
    pyautogui.write("Customer: John Doe")

    # Submit form
    pyautogui.press("enter")

    print("✅ Invoice processed successfully via RPA")

if __name__ == "__main__":
    automate_invoice_processing()
