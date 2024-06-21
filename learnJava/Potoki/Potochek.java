package Potoki;

import java.util.concurrent.atomic.AtomicLong;

public class Potochek implements Runnable {
    public int in1 = 0, in2 = 0;
    long help_result = 0;
    public static AtomicLong presult = new AtomicLong(0);
    int[] mass;

    Potochek(int in1, int in2, int mass[]) {
        this.in1 = in1;
        this.in2 = in2;
        this.mass = mass;
    }


    @Override
    public void run() {
        for (int i = in1; i < this.in2; i++) {
            this.help_result += this.mass[i];
        }
        presult.addAndGet(help_result);
    }

    public static void main(String[] args) throws InterruptedException {

        long result = 0;
        int[] mass = new int[100000];
        for (int i = 0; i < 100000; i++) {
            mass[i] = i;
        }
        ExecutionTimer timer1 = new ExecutionTimer();
        for(int i = 0; i < 100000; i++){
            result += mass[i];
        }
        timer1.end();
        System.out.println("Время работы main: " + timer1.duration());
        System.out.println("Cycle sum: " + result);
        int chunkSize = 100000 / 4; // Размер части массива для каждого потока

        Potochek[] potocheks = new Potochek[4];
        Thread[] threads = new Thread[4];

        for (int i = 0; i < 4; i++) {
            potocheks[i] = new Potochek(i * chunkSize, (i + 1) * chunkSize, mass);
            threads[i] = new Thread(potocheks[i]);
            threads[i].start();
        }
        ExecutionTimer timer2 = new ExecutionTimer();
        for (int i = 0; i < 4; i++) {
            threads[i].join(); // Ожидание завершения всех потоков
        }
        timer2.end();
        System.out.println("Time potoki: " + timer2.duration());
        System.out.println("Total sum: " + presult.get());
        if(timer2.duration() < timer1.duration()){
            System.out.println("Потоки и реально быстрее работают");
        }
        else System.out.println("Main быстрее, как так то(");
    }

}

