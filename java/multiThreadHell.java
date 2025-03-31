class EvenNum extends Thread {
	public void run() {

		for (int i = 2; i <= 20; i += 2) {
			System.out.println("even number:");
			System.out.println(i);

			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				System.out.println(e);
			}
		}
	}
}

class OddNum extends Thread {
	public void run() {
		for (int i = 1; i <= 20; i += 2) {
			System.out.println("odd number:");
			System.out.println(i);

			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				System.out.println(e);
			}
		}
	}
}

class multiThreadHell {
	public static void main(String[] args) {
		EvenNum even = new EvenNum();
		OddNum odd = new OddNum();

		even.start();
		odd.start();
	}
}
