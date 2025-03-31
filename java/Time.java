public class Time {
    int hour;
    int minute;
    int second;

    // Constructor
    Time(int hour, int minute, int second) {
        this.hour = hour;
        this.minute = minute;
        this.second = second;
        normalizeTime();
    }

    // Normalize time if seconds or minutes exceed 59
    private void normalizeTime() {
        if (second >= 60) {
            minute += second / 60;
            second %= 60;
        }
        if (minute >= 60) {
            hour += minute / 60;
            minute %= 60;
        }
    }

    // Display time in HH:MM:SS format
    void display() {
        System.out.printf("The time is %02d:%02d:%02d\n", hour, minute, second);
    }

    // Method to add two Time objects
    Time addTime(Time t) {
        int newHour = this.hour + t.hour;
        int newMinute = this.minute + t.minute;
        int newSecond = this.second + t.second;

        return new Time(newHour, newMinute, newSecond); // Will auto-normalize
    }

    // Method to subtract two Time objects
    Time subtractTime(Time t) {
        int totalSeconds1 = this.hour * 3600 + this.minute * 60 + this.second;
        int totalSeconds2 = t.hour * 3600 + t.minute * 60 + t.second;

        int diffInSeconds = Math.max(totalSeconds1 - totalSeconds2, 0); // Prevent negative time

        int newHour = diffInSeconds / 3600;
        int newMinute = (diffInSeconds % 3600) / 60;
        int newSecond = diffInSeconds % 60;

        return new Time(newHour, newMinute, newSecond);
    }

    public static void main(String[] args) {
        Time t1 = new Time(1, 20, 99); 
        Time t2 = new Time(2, 45, 30);

        System.out.println("Initial Times:");
        t1.display();
        t2.display();

        // Add times
        Time sum = t1.addTime(t2);
        System.out.println("\nAfter Addition:");
        sum.display();

        // Subtract times
        Time diff = t2.subtractTime(t1);
        System.out.println("\nAfter Subtraction:");
        diff.display();
    }
}
