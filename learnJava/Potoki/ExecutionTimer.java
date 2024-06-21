package Potoki;

public class ExecutionTimer {
    private long start;
    private long end;

    public ExecutionTimer() {
        reset();
        start = System.nanoTime();
    }

    public void end() {
        end = System.nanoTime();
    }

    public long duration() {
        return (end - start);
    }

    public void reset() {
        start = 0;
        end = 0;
    }
}
