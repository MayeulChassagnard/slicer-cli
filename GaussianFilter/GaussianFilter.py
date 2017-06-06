import SimpleITK as sitk

def GaussianFilter(image, sigma):
    print 'Gaussian filter was executed!'
    print 'received image of size:', image.GetSize()
    blurFilter = sitk.SmoothingRecursiveGaussianImageFilter()
    blurFilter.SetSigma(float(sigma))
    outimage = blurFilter.Execute(image)
    return outimage
