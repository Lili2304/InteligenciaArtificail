"ADptive LInear Neuron(adaline)"
import numpy as np
class adalineGD(object):
    "Parametros"

    def _int_(self,eta=0.01, n_inter=50,random_state=1):
        self.eta=eta
        self.n.inter=n_inter
        self.random_state=random_state

    def fit(self, X,y):
        rgen= np.random.RandomState(self.random_state)
        self.w_=rgen.normal(loc=0.0,scale=0.01,size=1 + X.shape[1])
        self.cost_=[]

        for i in range (self.n_iter):
            net_input = self.n_inter(x)
            output=self.activation(net_input)
            errors=(y - output)
            self.w_[1:]+=self.eta *X, T.dot(errors)
            self.w_[0]+= self.eta * errors.sum()
            cost = (errors**2).sum()/2.0
            self.cost_.append(cost)
        return self
    def net_input(self, X):
        return np.dot(X, self.w_[1:])+ self.w_[0]
    def activation(self,x):
        "calcula net imput"
        return np.dot(x,self.w_[1:]+ self.w_[0])
    def activation(self,X):
        "compute liear activation"
        return X
    def predict(self,x):
        "return class lebel after unit step"
        return np.where(self.activation(self.net_imput(x))>=0.0, 1, -1)
    


    