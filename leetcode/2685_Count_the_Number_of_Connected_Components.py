from collections import defaultdict

class Solution:
    def build_adj_mat(self, edges: list[list[int]]):
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        return adj
    
    def is_complete_component(self, component: list[int], adj: dict[int, set[int]]):
        # a connected component is said to be complete if there exists an edge
        # between every pair of vertices
        for i, a in enumerate(component):
            for b in component[i + 1:]:
                if b not in adj[a]:
                    return False
        return True


    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        num_connected_components = 0
        visited: list[int] = [ 0 for _ in range(n) ]
        adj = self.build_adj_mat(edges)

        for i in range(n):
            if visited[i]:
                continue
            stack = [i]
            component = [i]
            while stack:
                top = stack.pop()
                visited[top] = 1
                for v in adj[top]:
                    if visited[v]:
                        continue
                    component.append(v)
                    visited[v] = 1
                    stack.append(v)
            
            if self.is_complete_component(component, adj):
                num_connected_components += 1
        return num_connected_components
    
if __name__ == "__main__":
    s = Solution()
    print(s.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
    print(s.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))

