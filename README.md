# pauli_errors




**Tensor** Contains basic machinery to calculate the tensor product of an N qubit long discrete chain of Pauli Errors
Use strings like "xiyzixixxyzziiii" to represent these chains, their matrix will be represented by the TensorCompute method
Given a list of strings (i.e. a set of Pauli Errors) the **Errorlist** compiles an array (3 dimensional) of the corresponding matrices
**Subspace** takes the output of Errorlist and computes each matrix in the NC graph subspace by computing E_aE_b^* 

The uses for this are demonstrated in the other three files. In these, we assume one X,Y, or Z error on an arbitrary qubit. Then calculate the Errors and subspace generating elements. 

For n qubits, these generators create a subspace of M(2^n x 2^n). For each entry [i,j] in this space, we can calculate the nubmer of generators that span values at that entry, simply by adding each unique subspace generating element. 

While this method is valid for X errors, and likely Z errors, I don't know if it will work for Y errors since they give negative values under transposition

One interesting idea would be to add computation ability for arbitrary unitary of correct dimension U<xiyiixz>U* on either side of our tensored strings
