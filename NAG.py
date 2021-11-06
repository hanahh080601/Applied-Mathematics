import numpy as np 
np.random.seed(2)

X = np.random.rand(1000, 1)
y = 4 + 3 * X + .2*np.random.randn(1000, 1)

# Building Xbar 
one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_exact = np.dot(np.linalg.pinv(A), b)

def cost(w):
   N = Xbar.shape[0]
   y_hat = Xbar.dot(w)
   return 0.5 / N * np.linalg.norm(y - y_hat, 2)**2;

def grad(w):
   N = Xbar.shape[0]
   y_hat = Xbar.dot(w)
   return 1/N * Xbar.T.dot(y_hat - y)

def GD_NAG(w_init, grad, eta, gamma):
    w = [w_init]
    v = [np.zeros_like(w_init)]
    for it in range(100):
        v_new = gamma*v[-1] + eta*grad(w[-1] - gamma*v[-1])
        w_new = w[-1] - v_new
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:
            break
        w.append(w_new)
        v.append(v_new)
    return (w, it)

w_init = np.array([[2], [1]])
(w_mm, it_mm) = GD_NAG(w_init, grad, .5, 0.9)
print(it_mm, w_mm[-1])