package RSREU_controll_system;


public class Main {
    public static void main(String[] args) throws InterruptedException {
        Turnstile turnstile1 = new Turnstile(1,true, 1);
        Turnstile turnstile2 = new Turnstile(1,true, 2);
        Turnstile turnstile3 = new Turnstile(1,true, 3);
        for(int i = 1; i <= 100; i++) {
            new Thread(new Student(i, turnstile1, turnstile2, turnstile3)).start();
            Thread.sleep(400);
        }
        System.out.println("Максимальная длина очереди за время наблюдения за бедолагами была " + Turnstile.maxQueue);
    }
}

