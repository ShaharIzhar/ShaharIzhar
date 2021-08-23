/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation { // creates n-by-n grid, with all sites initially blocked
    boolean[][] grid = new boolean[0][0];
    private int len;
    private int top = 0;
    private int bottom;
    private WeightedQuickUnionUF uf;
    private int openSites = 0;

    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException();
        }
        grid = new boolean[n][n];
        uf = new WeightedQuickUnionUF(n * n + 1);
        len = n;
        bottom = len - 1;
        for (int j = 0; j < len; j++) {
            uf.union(len * len, j);
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (!grid[row][col]) {
            grid[row][col] = true;
            openSites++;
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        return grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        // StdOut.println("Row:" + row + " Col:" + col);
        if (isOpen(row, col)) {
            // StdOut.println("Connected One:" + row + col * len + " Two:" + (len * len - 1));

            if (uf.connected((row + col * len), (len * len - 1))) {
                // StdOut.println("Connected");
                return true;
            }
        }

        return false;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openSites;
    }

    // does the system percolate?
    public boolean percolates() {
        for (int j = 0; j < len; j++) {
            if (isFull(len - 1, j))
                return true;
        }
        return false;
    }

    public void printGrid() {
        StdOut.println("----------------------------------");
        for (int x = 0; x < len; x++) {
            for (int y = 0; y < len; y++) {
                String mark = isOpen(x, y) ? "0" : "X";
                StdOut.print("|" + mark + "|");
            }
            StdOut.println();
        }
        StdOut.println("----------------------------------");
    }

    public static void main(String[] args) {
        int tests = 1;
        int size = 5;
        int testedTimes = 1;
        int spaces = size * size - 1;
        int check = 0;
        int space = 0;
        while (testedTimes <= tests) {
            Percolation perc = new Percolation(size);
            perc.printGrid();
            while (!perc.percolates()) {
                int x = StdRandom.uniform(0, size);
                int y = StdRandom.uniform(0, size);

                perc.open(x, y);
                perc.printGrid();


            }//end while(!percolates())
            StdOut.println("NumberOfOpen: " + perc.numberOfOpenSites());
            testedTimes++;
        }//end while(TestedTimes<tests)
    }
}
