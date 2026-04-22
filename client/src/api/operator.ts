import type { Operator, OperatorCreate, OperatorUpdate } from '../types/operator'
import client from './client'


export const operatorApi = {
    list: () => {
        return client.get<Operator[]>('/operators/')
    },
    get: (operator_number: number) => {
        return client.get<Operator>(`/operators/${operator_number}`)
    },
    create: (operator: OperatorCreate) => {
        return client.post<Operator>('/operators/', operator)
    },
    update: (operator_number: number, data: OperatorUpdate) => {
        return client.patch<Operator>(`/operators/${operator_number}`, data)
    },
    delete: (operator_number: number) => {
        return client.delete(`/operators/${operator_number}`)
    }
}
export default operatorApi