package RSREU_controll_system;

public class Student implements Runnable{
    Turnstile turnstile1;
    Turnstile turnstile2;
    Turnstile turnstile3;
    public int studNum;
    public Student(int studNum, Turnstile turnstile1, Turnstile turnstile2,Turnstile turnstile3){
        this.studNum = studNum;
        this.turnstile1 = turnstile1;
        this.turnstile2 = turnstile2;
        this.turnstile3 = turnstile3;
    }
    @Override
    public void run() {
        System.out.printf("\tстудент %d зашел в вуз\n",
                studNum);
        Turnstile working_turnstile = Turnstile.findShortQueue(turnstile1, turnstile2, turnstile3);
        try {
            System.out.printf("\t\tстудент %d подошел к турникету и занял очередь у турникета %d\n",
                    studNum, working_turnstile.numberTurnstile);
            working_turnstile.acquire();
            System.out.printf("\t\t\tпришла очередь студента %d, он думает о смысле жизни\n",
                    studNum);
            Thread.sleep((int)(Math.random()*10+1)*200 + 150);
            working_turnstile.release();
            System.out.printf("\t\t\t\tстудент %d тяжело выдохнул, покинул турникет %d и пошел дальше\n",
                    studNum, working_turnstile.numberTurnstile);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

}
