import java.util.Scanner;

public class ATM {
    public static void main(String[] args) {
        // Initialize balance, withdrawal, and deposit variables
        int balance = 100000, withdraw, deposit;
        Scanner sc = new Scanner(System.in);

        while (true) {
            // Display ATM menu
            System.out.println("Automated Teller Machine");
            System.out.println("Choose 1 for Withdraw");
            System.out.println("Choose 2 for Deposit");
            System.out.println("Choose 3 for Check Balance");
            System.out.println("Choose 4 for EXIT");
            System.out.print("Choose the operation you want to perform: ");
            
            // Get user choice
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    // Withdrawal
                    System.out.print("Enter money to be withdrawn: ");
                    withdraw = sc.nextInt();
                    if (balance >= withdraw) {
                        balance -= withdraw;
                        System.out.println("Please collect your money");
                    } else {
                        System.out.println("Insufficient Balance");
                    }
                    break;

                case 2:
                    // Deposit
                    System.out.print("Enter money to be deposited: ");
                    deposit = sc.nextInt();
                    balance += deposit;
                    System.out.println("Your money has been successfully deposited");
                    break;

                case 3:
                    // Check balance
                    System.out.println("Balance: ₹" + balance);
                    break;

                case 4:
                    // Exit
                    System.out.println("Thank you for using the ATM!");
                    sc.close();
                    System.exit(0);
                    break;

                default:
                    System.out.println("Invalid choice! Please choose a valid option.");
            }
        }
    }
}
