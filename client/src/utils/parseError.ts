

export const parseError = (err: unknown, fallback = 'Something went wrong'): string => {
  console.log("got this error",`${err}`)
  if (
    typeof err === 'object' &&
    err !== null &&
    'response' in err
  ) {

    const detail = (err as { response: { data?: { detail?: unknown } } }).response?.data?.detail
    if (Array.isArray(detail)) {
      return detail.map(d => d.msg).join(', ')
    }
    if (typeof(detail) === 'string'){
        return detail
    }
  }
  return fallback
}