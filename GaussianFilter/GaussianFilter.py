import SimpleITK as sitk

import logging
logging.basicConfig(level=logging.CRITICAL)

from ctk_cli import CLIArgumentParser

def main(args):
    inputImage = sitk.ReadImage(args.inputImageFile)
    blurFilter = sitk.SmoothingRecursiveGaussianImageFilter()
    blurFilter.SetSigma(float(args.sigma))
    outputImage = blurFilter.Execute(inputImage)
    sitk.WriteImage(outputImage, args.outputImageFile)

if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())
