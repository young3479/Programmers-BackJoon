import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Solution {

    private static class Node { //node 클래스 
        int dest, cost;

        public Node(int dest, int cost) {
            this.dest = dest; //다른 노드(목적지)
            this.cost = cost; //비용(거리)
        }
    }

    public int solution(int N, int[][] road, int K) {
        ArrayList<Node>[] adjList = new ArrayList[N + 1]; //인접리스트(연결관계저장)
        for (int i = 1; i <= N; i++) {
            adjList[i] = new ArrayList<>(); //각 노드에 대해 초기화
        }

        for (int[] edge : road) { //도로 정보 추가 (양방향)
            adjList[edge[0]].add(new Node(edge[1], edge[2]));
            adjList[edge[1]].add(new Node(edge[0], edge[2]));
        }

        int[] dist = new int[N + 1]; //최단 거리 저장 배열
        Arrays.fill(dist, Integer.MAX_VALUE); //초기: 모든 거리 무한대

				//우선 순위 큐
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        pq.add(new Node(1, 0)); //1번 노드 추가
        dist[1] = 0; //1번 노드를 시작 노드로

        while (!pq.isEmpty()) { //다익스트라 알고리즘
            Node now = pq.poll(); //현재 노드 큐에서 꺼내기

						//현재 노드까지의 거리가 이미 저장된 거리보다 크면 건너뜀
            if (dist[now.dest] < now.cost)
                continue;

						//인접한 노드들을 탐색하면서, 더 짧은 경로가 발견되면 dist 배열을 업데이트하고 우선순위 큐에 추가
            for (Node next : adjList[now.dest]) {
                if (dist[next.dest] > now.cost + next.cost) {
                    dist[next.dest] = now.cost + next.cost;
                    pq.add(new Node(next.dest, dist[next.dest]));
                }
            }
        }

        int answer = 0;

				//K 이하의 거리인 노드 개수 계산
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= K) answer++;
        }

        return answer;
    }

}