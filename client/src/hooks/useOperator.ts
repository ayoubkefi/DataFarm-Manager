import { useState, useEffect } from "react"
import operatorApi from "../api/operator"
import type  { Operator } from "../types/operator"

interface UseOperatorResult {
    operators : Operator[]
    loading : boolean
    error : string | null
    referesh : () => void 
}

export const useOperators = () : UseOperatorResult  => {
    const [operators,setOperators] =  useState<Operator[]>([])
    const [loading,  setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetch  = async() => {
        setLoading(true)
        setError(null)
        try{
            const res = await operatorApi.list()
            setOperators(res.data)
        } catch{
            setError('Failed to load operators')
        } finally{
            setLoading(false)
        }

    }
    useEffect(()=>{
    fetch()
        },[])
    return {operators, loading, error, referesh : fetch}
}
