/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] rq;
    private int numberOfItems = 0;

    // construct an empty randomized queue
    public RandomizedQueue() {
        this.numberOfItems = 0;
        this.rq = (Item[]) new Object[1];
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private int i = numberOfItems;
        private int[] order;

        public RandomizedQueueIterator() {
            order = new int[i];
            for (int j = 0; j < i; ++j) {
                order[j] = j;
            }
            StdRandom.shuffle(order);
        }

        public boolean hasNext() {
            return i > 0;
        }

        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();
            return rq[order[--i]];
        }
    }

    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < numberOfItems; i++)
            copy[i] = rq[i];
        rq = copy;
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return numberOfItems == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return numberOfItems;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) throw new NullPointerException();

        rq[numberOfItems++] = item;
        if (numberOfItems == rq.length)
            resize(2 * rq.length);

    }


    // remove and return a random item
    public Item dequeue() {
        if (numberOfItems == 0) throw new java.util.NoSuchElementException();

        int randomNumber = StdRandom.uniform(numberOfItems);
        Item oldItem = rq[randomNumber];
        rq[randomNumber] = rq[numberOfItems - 1];
        rq[--numberOfItems] = null;
        if (numberOfItems > 0 && numberOfItems == rq.length / 4)
            resize(rq.length / 2);
        return oldItem;

    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (numberOfItems == 0) throw new java.util.NoSuchElementException();

        int randomNumber = StdRandom.uniform(numberOfItems - 1);
        return rq[randomNumber];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    // unit testing (required)
    public static void main(String[] args) {
    }
}
