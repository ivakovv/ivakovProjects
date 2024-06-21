package Philosophers;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class Philosopher implements Runnable {
    private Object leftFork;
    private Object rightFork;
    public Philosopher(Object leftFork, Object rightFork) {
        this.leftFork = leftFork;
        this.rightFork = rightFork;
    }
    @Override
    public void run() {
        try {
            while (true) {
                LocalTime currentTime = LocalTime.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss:SSS:nnnnnnnnn");
                doSomething(currentTime.format(formatter) + ": Думает");
                synchronized (leftFork) {
                    doSomething(currentTime.format(formatter) + ": Взял левую вилку");
                    synchronized (rightFork) {
                        doSomething(currentTime.format(formatter) + ": Взял правую вилку - трапезничает");
                        doSomething(currentTime.format(formatter) + ": Положил правую вилку");
                    }
                    doSomething(currentTime.format(formatter) + ": Положил левую вилку. Думает о великом дальше");
                }
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    private void doSomething(String action) throws InterruptedException {
        System.out.println(Thread.currentThread().getName() + " " + action);
        Thread.sleep(((int) (Math.random() * 1000)));
    }
}