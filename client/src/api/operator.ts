import type { Operator, OperatorCreate, OperatorUpdate } from '../types/operator'
import client from './client'


export const operatorApi = {
    list : ()  =>  {
        client.get<Operator[]>('/operators/')
    },
    get : (operator_number : number) => {
        client.get<Operator>(`/operators/${operator_number}`)
    },
    create : (operator : OperatorCreate) => {
        client.post<Operator>(`/operators/${operator}`)
    },
    update : (operator_number : number, data : OperatorUpdate) => {
        client.patch<Operator>(`/operators/${operator_number}`,data)
    },
    delete : (operator_number : number) => {
        client.delete(`/operators/${operator_number}`)
    }
}