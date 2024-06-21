package RSREU_controll_system;

import java.util.concurrent.Semaphore;

public class Turnstile extends Semaphore {
    public static int maxQueue;
    public int numberTurnstile;

    public Turnstile(int permits, boolean fair, int numberTurnstile) {
        super(permits, fair);
        this.numberTurnstile = numberTurnstile;
    }
    synchronized public static Turnstile findShortQueue(Turnstile turnstile1, Turnstile turnstile2,Turnstile turnstile3) {
        int queue1 = turnstile1.getQueueLength();
        int queue2 = turnstile2.getQueueLength();
        int queue3 = turnstile3.getQueueLength();
        if (queue1 >= queue2 & queue1 >= queue3) {
            if(queue1 > Turnstile.maxQueue)
                Turnstile.maxQueue = queue1;
        }
        else if (queue2 >= queue1 & queue2 >= queue3) {
            if(queue2 > Turnstile.maxQueue)
                Turnstile.maxQueue = queue2;
        }
        else {
            if(queue3 > Turnstile.maxQueue)
                Turnstile.maxQueue = queue3;
        }
        //System.out.println("МАКС ДЛИНА ОЧЕРЕДИ " + maxQueue);
        if (queue1 <= queue2 & queue1 <= queue3) {
            return turnstile1;
        }
        else if (queue2 <= queue1 & queue2 <= queue3) {
            return turnstile2;
        }
        else {
            return turnstile3;
        }
    }
}
