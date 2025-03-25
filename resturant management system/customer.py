
import time
import datetime

def update_sales_and_feedback(total_amount, feedback_text):
    # Get current month
    current_month = datetime.datetime.now().strftime("%B")  # e.g., "January", "February"
    current_month_sales_key = f"sales of {current_month.lower()}:"
    
    # Read existing data
    try:
        with open("sales_feedback.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    
    # Process the file
    in_sales_section = False
    in_feedback_section = False
    sales_updated = False
    new_lines = []
    
    for line in lines:
        line = line.strip()
        
        # Handle section headers
        if line.lower() == "sales":
            in_sales_section = True
            in_feedback_section = False
            new_lines.append("sales")
            continue
        elif line.lower() == "feedback":
            in_sales_section = False
            in_feedback_section = True
            new_lines.append("feedback")
            continue
        
        # Update sales if in sales section
        if in_sales_section and line.startswith(current_month_sales_key):
            try:
                current_sales = float(line.split(":")[1].strip())
                new_sales = current_sales + total_amount
                new_lines.append(f"{current_month_sales_key}{new_sales}")
                sales_updated = True
            except (IndexError, ValueError):
                new_lines.append(line)
        elif in_sales_section:
            new_lines.append(line)
        elif in_feedback_section:
            new_lines.append(line)
    
    # If current month sales wasn't found, add it
    if not sales_updated:
        if "sales" not in [l.lower() for l in new_lines]:
            new_lines.append("sales")
        new_lines.append(f"{current_month_sales_key}{total_amount}")
    
    # Add feedback
    if "feedback" not in [l.lower() for l in new_lines]:
        new_lines.append("feedback")
    new_lines.append(feedback_text)
    
    # Write back to file
    with open("sales_feedback.txt", "w") as file:
        file.write("\n".join(new_lines) + "\n")

def load_menu(filename):
    menu = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.endswith(':'):  # Skip empty lines and category headers
                continue
                
            # Split dish name and price
            parts = line.rsplit(':', 1)
            if len(parts) == 2:
                dish = parts[0].strip()
                price = float(parts[1].strip())
                menu[dish.lower()] = price
    
    return menu
def save_order(ordered_items):
    with open("order.txt", "a") as f:
        for item in ordered_items:
            f.write(f"{item}\n")
        f.write("\n") 
def calculate_order(menu):
    total = 0.0
    ordered_items = [] 
    
    print("Welcome to our restaurant!")
    print("Enter the dishes you'd like to order (one per line).")
    print("Type 'done' when you're finished.\n")
    
    while True:
        dish = input("Enter dish name: ").strip().lower()
        if dish == 'done':
            break
        
        if dish in menu:
            ordered_items.append(dish.title())  # Only store the name
            total += menu[dish]
            print(f"Added {dish.title()} (${menu[dish]:.2f}) to your order.")
        else:
            print(f"Sorry, we don't have '{dish.title()}'. Please try again.")
    
    return ordered_items, total  # Returns (list of names, total)
def customer_main():
   print("Welcome customer!!")
   with open("menu.txt","r") as menuu:
      print(menuu.read())
   menu_file = "menu.txt"
   menu = load_menu(menu_file)
      
   if not menu:
      print("Error: Could not load menu. Please check the menu file.")
         
      
   ordered_items, total = calculate_order(menu)
   save_order(ordered_items)
      
      # Display simplified order summary
   print("\nYour order summary:")
   for item_name in ordered_items:
         print(f"- {item_name}")
   print(f"\nTotal amount: ${total:.2f}")
   payment=int(input("Please pay to confirm your order:"))
   if payment < total:
         print("Insufficient payment! Please try again.")
         return
   elif payment > total:
       change=payment-total
       print("Payment successful! Thank you for dining with us.")
       print(f"Here is your Change: ${change:.2f}")
   else:
       print("Payment successful! Thank you for dining with us.")
      
   print("\nChecking your order status...")
   time.sleep(2)
   
   orderrr = input("Do you want to see your order status? (y/n): ")
   if orderrr.lower() == "y":
        try:
            with open("order_status.txt", "r") as status_file:
                status = status_file.read().strip()
                if status == "complete":
                    print("Your order is complete! Thank you for dining with us.")
                    with open("order_status.txt", "w") as status_file:
                        print("")
                else:
                    print("Your order is still in progress. Please wait...")
        except FileNotFoundError:
            print("Your order status is not available yet. Please check back later.")
   feedback = input("Please give feedback on our service: ")
   if feedback.strip():  # Only update if feedback is not empty
        update_sales_and_feedback(total, feedback)
        print("Thank you for your feedback!")
   
   
if __name__ == "__main__":
    customer_main()