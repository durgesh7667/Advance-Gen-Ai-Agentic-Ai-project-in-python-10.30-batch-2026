{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2cb9ccdf-5e60-40c5-9664-64b85b72fa52",
   "metadata": {},
   "source": [
    "# array manipulations function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c494b2a4-78c9-430e-86b9-98f6dd4ed989",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "28e10a10-bb0b-4ac5-99e1-f78965fd3df7",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'builtin_function_or_method' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m a1=\u001b[43mnp\u001b[49m\u001b[43m.\u001b[49m\u001b[43marray\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m1\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m2\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m3\u001b[39;49m\u001b[43m]\u001b[49m\n\u001b[32m      2\u001b[39m reshaped=[a1,(\u001b[32m1\u001b[39m,\u001b[32m3\u001b[39m)]\n",
      "\u001b[31mTypeError\u001b[39m: 'builtin_function_or_method' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "a1=np.array[1,2,3]\n",
    "reshaped=[a1,(1,3)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "57d80bef-0268-4d03-ac3a-4a72f09be750",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "array() takes from 1 to 2 positional arguments but 4 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m f1=\u001b[43mnp\u001b[49m\u001b[43m.\u001b[49m\u001b[43marray\u001b[49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m1\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m2\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m3\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m4\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m5\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m6\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\u001b[43m[\u001b[49m\u001b[32;43m7\u001b[39;49m\u001b[43m,\u001b[49m\u001b[32;43m8\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m      2\u001b[39m flattened=np.ravel(f1)\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mFlattened array:\u001b[39m\u001b[33m\"\u001b[39m,flattened)\n",
      "\u001b[31mTypeError\u001b[39m: array() takes from 1 to 2 positional arguments but 4 were given"
     ]
    }
   ],
   "source": [
    "f1=np.array([1,2],[3,4],[5,6],[7,8])\n",
    "flattened=np.ravel(f1)\n",
    "print(\"Flattened array:\",flattened)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f3c1d19e-94a1-4865-adda-c75902fefe3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Added 2 to g: [3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "# Add two arrays\n",
    "g=np.array([1,2,3,4])\n",
    "added=np.add(g,2)\n",
    "print(\"Added 2 to g:\", added)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "44d5d988-21b8-4c0b-98e7-858235c39410",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'sqrt_val' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[11]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m# Square each element\u001b[39;00m\n\u001b[32m      2\u001b[39m squared=np.power(g,\u001b[32m2\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33msquared g:\u001b[39m\u001b[33m\"\u001b[39m,\u001b[43msqrt_val\u001b[49m)\n",
      "\u001b[31mNameError\u001b[39m: name 'sqrt_val' is not defined"
     ]
    }
   ],
   "source": [
    "# Square each element\n",
    "squared=np.power(g,2)\n",
    "print(\"squared g:\",sqrt_val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ff81bda7-95cd-4a37-91f3-cb87ad69554e",
   "metadata": {},
   "outputs": [
    {
     "ename": "_IncompleteInputError",
     "evalue": "incomplete input (3715707090.py, line 3)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[12]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mprint(\u001b[39m\n          ^\n\u001b[31m_IncompleteInputError\u001b[39m\u001b[31m:\u001b[39m incomplete input\n"
     ]
    }
   ],
   "source": [
    "a3=np.array([1,2,3])\n",
    "dot_product=np.dot(a1,g)\n",
    "print("
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "53f10a40-fc81-4d59-9076-dfb98668700a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean of s: 2.5\n"
     ]
    }
   ],
   "source": [
    "s=np.array([1,2,3,4])\n",
    "mean=np.mean(s)\n",
    "print(\"Mean of s:\", mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a1cf1d0a-8f00-48b7-9b5f-001b123a43e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Standard deviation of s: 1.118033988749895\n"
     ]
    }
   ],
   "source": [
    "std_dev=np.std(s)\n",
    "print(\"Standard deviation of s:\", std_dev)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fbbde4aa-23a3-46c9-b948-6025cf6a0268",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random values: [0.16839729 0.591937   0.50761524]\n"
     ]
    }
   ],
   "source": [
    "random_vals=np.random.rand(3)\n",
    "print(\"Random values:\", random_vals)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b1f7badc-1e45-4ce3-af26-5e010694f006",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random values: [0.16839729 0.591937   0.50761524]\n"
     ]
    }
   ],
   "source": [
    "np.random.seed(0)\n",
    "andom_vals=np.random.rand(3)\n",
    "print(\"Random values:\", random_vals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f7f200cb-8daf-4ba8-a71a-0f3c4b41207d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'rand' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[22]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m np.random.seed(\u001b[32m0\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[43mrand\u001b[49m.ints=np.random.randint(\u001b[32m0\u001b[39m,\u001b[32m10\u001b[39m,size=\u001b[32m5\u001b[39m)\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mRandom integers:\u001b[39m\u001b[33m\"\u001b[39m, rand_ints)\n",
      "\u001b[31mNameError\u001b[39m: name 'rand' is not defined"
     ]
    }
   ],
   "source": [
    "np.random.seed(0)\n",
    "rand.ints=np.random.randint(0,10,size=5)\n",
    "print(\"Random integers:\", rand_ints)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c912578-d662-4c12-95fc-71ac9bfbd27a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60cb7221-889c-4585-89b4-507666755f16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
